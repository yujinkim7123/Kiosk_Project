package com.inburger.backend.services;

import com.inburger.backend.models.Menu;

import java.util.List;

public interface MenuService {

    List<Menu> getAllMenu();
    Menu getMenuDetail(long id);
}
