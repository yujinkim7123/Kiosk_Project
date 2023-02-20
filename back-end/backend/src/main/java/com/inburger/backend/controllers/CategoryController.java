package com.inburger.backend.controllers;

import com.inburger.backend.models.Category;
import com.inburger.backend.repositories.CategoryRepository;
import com.inburger.backend.services.CategoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(path="/inburger")
public class CategoryController {

    private CategoryRepository categoryRepository;
    private CategoryService categoryService;

    @Autowired
    public CategoryController(CategoryRepository categoryRepository,
                              CategoryService categoryService) {
        this.categoryService = categoryService;
        this.categoryRepository = categoryRepository;
    }

    // 모든 재료 죠회
    @GetMapping(value="/category")
    public List<Category> getAllCategory() {
        return categoryService.getAllCategory();
    }

}
