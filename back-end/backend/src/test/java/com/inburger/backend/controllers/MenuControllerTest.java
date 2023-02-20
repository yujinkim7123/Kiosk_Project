package com.inburger.backend.controllers;

import com.inburger.backend.models.Category;
import com.inburger.backend.models.Menu;
import com.inburger.backend.repositories.MenuRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class MenuControllerTest {

    private MenuRepository menuRepository;


    @AfterEach
    public void cleanUp() {
        menuRepository.deleteAll();
    }

    @BeforeAll

    @BeforeEach
    void setUp() {
        String name = "hamburger";
        Category category = new Category();
        category.setName(name);

        //when
    }

    @Test
    void createMenu() {
        int category_id = 1;
        String name = "burger_1";





        Menu menu = new Menu();

    }

    @Test
    void getAllMenu() {
    }
}