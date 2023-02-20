package com.inburger.backend.controllers;

import com.inburger.backend.exceptions.ResourceNotFoundException;
import com.inburger.backend.models.*;
import com.inburger.backend.repositories.MenuRepository;
import com.inburger.backend.repositories.OrderDetailRepository;
import com.inburger.backend.repositories.OrderRepository;
import com.inburger.backend.repositories.UserRepository;
import com.inburger.backend.services.MenuService;
import com.inburger.backend.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@RestController
@RequestMapping(path = "/inburger")
//@CrossOrigin("http://i8a203.p.ssafy.io/")
@CrossOrigin("http://3.36.49.220/")
//@CrossOrigin("http://70.12.246.87:3000/")
public class MenuController {

    private UserService userService;
    private final UserRepository userRepository;

    private MenuService menuService;
    private final MenuRepository menuRepository;

    private OrderRepository orderRepository;
    private OrderDetailRepository orderDetailRepository;

    @Autowired
    public MenuController(MenuService menuService,
                          MenuRepository menuRepository,
                          UserRepository userRepository,
                          UserService userService,
                          OrderRepository orderRepository,
                          OrderDetailRepository orderDetailRepository) {
        this.menuRepository = menuRepository;
        this.menuService = menuService;
        this.userRepository = userRepository;
        this.userService = userService;
        this.orderRepository = orderRepository;
        this.orderDetailRepository = orderDetailRepository;
    }

    @GetMapping(value = "/menu")
    public List<Menu> getAllMenu() {
        return menuService.getAllMenu();
    }

    // 메뉴 저장
    @PostMapping(value="/menu")
    public Menu createMenu(@RequestBody Menu menu) {
        return menuRepository.save(menu);
    }

    // 유저 정보를 받고 메뉴 + 유저 정보 전달
    @PostMapping(value="/menu/user")
    public List<Object> getAllMenu(@RequestBody User user) {
//        HashMap<String, List> returnMenu= new HashMap<>();
//        returnMenu.put("User", userService.getAllUser());
//        returnMenu.put("Menu", menuService.getAllMenu());
        // 추천 메뉴 검색
        // 해당 유저 검색
        if (user.getName() == "none") {
            return null;
        }
        User order_user = userService.saveUser(user);

//        User order_user = userRepository.findById(id).orElseThrow(()->
//                new ResourceNotFoundException("user", "id", id));

        // 해당 유저의 history 조회
        System.out.println(order_user);
        List<Order> historyList = order_user.getHistory();
        System.out.println(historyList);

        List<MenuDTO> oddList = new ArrayList<>();

        // order-detail_menuDTO list
        for (Order o : historyList) {
            for (OrderDetail od : o.getOrderDetails()){
                int customPrice;
                List<CustomDTO> customDTOList = od.getCustoms().stream().map(custom ->
                        (CustomDTO.builder()
                                    .ingredientCount(custom.getCount())
                                    .ingredientName(custom.getIngredient().getName())
                                    .build())).collect(Collectors.toList());
                customPrice = od.getPrice();
            MenuDTO menuDTO = MenuDTO.builder()
                            .menuCustomDTO(customDTOList)
                            .menuName(od.getMenu().getName())
                            .customPrice(customPrice)
                            .build();
            oddList.add(menuDTO);
            }
        }

        // 각 oddList 에서 중복 제거 개수 세서 저장
        Map<MenuDTO, Integer> result = new HashMap<>();
        for(MenuDTO od : new HashSet<>(oddList)) {
            result.put(od, Collections.frequency(oddList, od));
        }


        // 주문 많은 순서로 정렬
        List<Map.Entry<MenuDTO, Integer>> entryList = new LinkedList<>(result.entrySet());
        entryList.sort(new Comparator<Map.Entry<MenuDTO, Integer>>() {
            @Override
            public int compare(Map.Entry<MenuDTO, Integer> o1, Map.Entry<MenuDTO, Integer> o2) {
                return o2.getValue() - o1.getValue();
            }
        });

        // 만약 추천이 일정 개수 이하면 더 추가해줌
        if (result.size() < 9) {
            // 전체 주문 조회
            List<Order> totalOrder = orderRepository.findAll();
            List<MenuDTO> totalOddList = new ArrayList<>();
            for (Order o : totalOrder) {
                Integer customPrice;
                for (OrderDetail od : o.getOrderDetails()){
                    List<CustomDTO> customDTOList2 = od.getCustoms().stream().map(custom ->
                            (CustomDTO.builder()
                                    .ingredientCount(custom.getCount())
                                    .ingredientName(custom.getIngredient().getName())
                                    .build())).collect(Collectors.toList());
                    customPrice = od.getPrice();
                MenuDTO menuDTO = MenuDTO.builder()
                        .menuCustomDTO(customDTOList2)
                        .menuName(od.getMenu().getName())
                        .customPrice(customPrice)
                        .build();
                totalOddList.add(menuDTO);
                }
            }

            // 갯수 세서 저장
            Map<MenuDTO, Integer> result2 = new HashMap<>();
            for(MenuDTO od : new HashSet<>(totalOddList)) {
                result2.put(od, Collections.frequency(totalOddList, od));
            }

            List<Map.Entry<MenuDTO, Integer>> entryList2 = new LinkedList<>(result2.entrySet());
            entryList2.sort(new Comparator<Map.Entry<MenuDTO, Integer>>() {
                @Override
                public int compare(Map.Entry<MenuDTO, Integer> o1, Map.Entry<MenuDTO, Integer> o2) {
                    return o2.getValue() - o1.getValue();
                }
            });

            entryList2.removeAll(entryList);
            if (entryList2.size() != 0) {
                for (int i = 0; i < 9 - entryList.size() && i < entryList2.size(); i++) {
                    entryList.add(entryList2.get(i));
                }
            }
        }
        List<Object> resultRecommend = new ArrayList<>();

        if (!entryList.isEmpty()) {
            for (Map.Entry<MenuDTO, Integer> i : entryList) {
                resultRecommend.add(
                        Recommend.builder()
                                .menuName(i.getKey().getMenuName())
                                .ingredientList(i.getKey().getMenuCustomDTO())
                                .menuPrice(i.getKey().getCustomPrice())
                                .build()
                );
            }
        }
        return resultRecommend;
    }

    // 메뉴 하나 반환
    @GetMapping(value="/menu/{id}")
    public ResponseEntity<Menu> getMenuDetail(@PathVariable("id") Long id) {
        Menu menu = menuService.getMenuDetail(id);
        return ResponseEntity.ok(menu);
    }

    // 메뉴 수정
    @PostMapping(value="/menu/{id}")
    public ResponseEntity<Menu> updateMenu(@PathVariable("id") Long id, @RequestBody Menu menuDetail) {
        Menu menu = menuService.getMenuDetail(id);

        menu.setName(menuDetail.getName());
        menu.setCategory(menuDetail.getCategory());
        menu.setPrice(menuDetail.getPrice());

        Menu updatedMenu = menuRepository.save(menu);
        return ResponseEntity.ok(updatedMenu);
    }

    //메뉴 삭제
    @DeleteMapping(value="/menu/{id}")
    public void deleteMenu(@PathVariable("id") Long id) {
        menuRepository.deleteById(id);
    }
}
