package com.inburger.backend.services;

import com.inburger.backend.models.Custom;
import com.inburger.backend.models.OrderDetail;

import java.util.List;

public interface CustomService {

    List<Custom> getAllCustom();
    Custom saveCustom(String name, int count, long orderDetailId);
}
