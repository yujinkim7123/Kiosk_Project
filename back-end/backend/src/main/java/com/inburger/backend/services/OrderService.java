package com.inburger.backend.services;

import com.inburger.backend.models.Order;

import java.util.List;

public interface OrderService {

    List<Order> getAllOrder();
    Order saveOrder(Order order, Long id);
}
