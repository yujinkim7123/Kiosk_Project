package com.inburger.backend.controllers;

import com.inburger.backend.models.Order;
import com.inburger.backend.models.OrderDetail;
import com.inburger.backend.repositories.OrderDetailRepository;
import com.inburger.backend.services.OrderDetailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Collection;
import java.util.List;

@RestController
@RequestMapping(path = "/inburger")
public class OrderDetailController {

    private OrderDetailService orderDetailService;
    private final OrderDetailRepository orderDetailRepository;

    @Autowired
    public OrderDetailController(OrderDetailService orderDetailService,
                                 OrderDetailRepository orderDetailRepository) {
        this.orderDetailRepository = orderDetailRepository;
        this.orderDetailService = orderDetailService;
    }
    //전체 상새 주문 조회
    @GetMapping(value = "/order-detail")
    public List<OrderDetail> getAllOrderDetail() {
        return orderDetailService.getAllOrderDetail();
    }

    // 주문 하기 (상세 주문 1개 생성)
//    @PostMapping(value = "/order-detail")
//    public ResponseEntity<OrderDetail> createOrderDetail(@RequestBody OrderDetail orderDetail) {
//        return new ResponseEntity<OrderDetail>(orderDetailService.saveOrderDetail(orderDetail), HttpStatus.CREATED);
//    }

    // 주문에 해당되는 모든 상세 주문 조회
    @GetMapping(value = "/order-detail/details/{id}")
    public Collection<OrderDetail> getAllOrderDetailByOrderId(@PathVariable("id") long id) {
        return orderDetailService.getAllOrderDetailBiId(id);
    }

    // 상세 주문 보기(1개)
    @GetMapping(value = "/order-detail/{id}")
    public OrderDetail getOrderDetailById(@PathVariable("id") long id ) {
        return orderDetailService.getOrderDetailById(id);
    }

}
