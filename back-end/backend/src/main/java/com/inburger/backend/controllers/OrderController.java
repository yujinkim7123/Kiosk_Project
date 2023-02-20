package com.inburger.backend.controllers;

import com.inburger.backend.models.Custom;
import com.inburger.backend.models.Order;
import com.inburger.backend.models.OrderDTO;
import com.inburger.backend.models.OrderDetail;
import com.inburger.backend.repositories.OrderDetailRepository;
import com.inburger.backend.repositories.OrderRepository;
import com.inburger.backend.services.OrderDetailService;
import com.inburger.backend.services.OrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping(path="/inburger")
@CrossOrigin("http://3.36.49.220:3000/")
public class OrderController {

    private final OrderRepository orderRepository;
    private final OrderDetailRepository orderDetailRepository;
    private OrderService orderService;
    private OrderDetailService orderDetailService;

    @Autowired
    public OrderController(OrderRepository orderRepository,
                           OrderService orderService,
                           OrderDetailRepository orderDetailRepository,
                           OrderDetailService orderDetailService) {
        this.orderRepository = orderRepository;
        this.orderService = orderService;
        this.orderDetailRepository = orderDetailRepository;
        this.orderDetailService = orderDetailService;
    }

    @GetMapping(value="/order")
    public List<Order> getAllOrder() {
        return orderService.getAllOrder();
    }

    // 주문과 유저 정보를 받아서 저장
    @PostMapping(value = "/order")
    public List<OrderDetail> createOrder(@RequestBody OrderDTO orderDTO) {
        // 전체 order 주문 저장
        Order newOrder = orderService.saveOrder(orderDTO.getOrder(), orderDTO.getUser_id());

        // 전체 order에 따른 orderDetail들을 생성
        List<OrderDetail> newOrderDetails = orderDTO.getOrderDetailDTO().stream().map(od ->
                orderDetailService.saveOrderDetail(od, newOrder.getId())).collect(Collectors.toList());
        return newOrderDetails;

        // 각 OrderDetail에 맞는 Custom을 등록

    }
}
