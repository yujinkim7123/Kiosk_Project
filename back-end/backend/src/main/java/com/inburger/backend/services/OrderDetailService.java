package com.inburger.backend.services;

import com.inburger.backend.models.OrderDetail;
import com.inburger.backend.models.OrderDetailDTO;

import java.util.Collection;
import java.util.List;

public interface OrderDetailService {

    List<OrderDetail> getAllOrderDetail();
    Collection<OrderDetail> getAllOrderDetailBiId(Long orderId);
    OrderDetail saveOrderDetail(OrderDetailDTO orderDetailDTO, Long orderId);
    OrderDetail getOrderDetailById(long id);
}
