package com.inburger.backend.repositories;

import com.inburger.backend.models.Menu;
import com.inburger.backend.models.Order;
import com.inburger.backend.models.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {


    List<Order> findOrdersByUser(User user);



}
