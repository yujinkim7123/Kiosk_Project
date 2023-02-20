package com.inburger.backend.repositories;

import com.inburger.backend.models.OrderDetail;
import com.inburger.backend.models.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Collection;
import java.util.List;

public interface OrderDetailRepository extends JpaRepository<OrderDetail, Long> {

    Collection<OrderDetail> findByOrderId(long orderId);

//    List<OrderDetail> findOrderDetailsByUserId(User userId);
}
