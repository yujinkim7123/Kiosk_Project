package com.inburger.backend.services.servicesImpl;

import com.inburger.backend.exceptions.ResourceNotFoundException;
import com.inburger.backend.models.Order;
import com.inburger.backend.models.User;
import com.inburger.backend.repositories.OrderRepository;
import com.inburger.backend.repositories.UserRepository;
import com.inburger.backend.services.OrderService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class OrderServiceImpl implements OrderService {

    private OrderRepository orderRepository;
    private UserRepository userRepository;

    public OrderServiceImpl(OrderRepository orderRepository,
                            UserRepository userRepository) {
        super();
        this.orderRepository = orderRepository;
        this.userRepository = userRepository;
    }

    @Override
    public List<Order> getAllOrder() {
        return orderRepository.findAll();
    }

    @Override
    public Order saveOrder(Order order, Long id) {
        User user = userRepository.findById(id).orElseThrow(() ->
           new ResourceNotFoundException("User", "Userid", id)
        );
        Order new_order = Order.builder()
                .isPackaging(order.getIsPackaging())
                .count(order.getCount())
                .price(order.getPrice())
                .orderDate(order.getOrderDate())
                .user(user)
                .build();
        return orderRepository.save(new_order);
    }
}
