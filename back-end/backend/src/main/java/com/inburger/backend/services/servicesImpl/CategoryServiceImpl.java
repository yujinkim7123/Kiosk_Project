package com.inburger.backend.services.servicesImpl;

import com.inburger.backend.models.Category;
import com.inburger.backend.models.Custom;
import com.inburger.backend.repositories.CategoryRepository;
import com.inburger.backend.services.CategoryService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoryServiceImpl implements CategoryService {

    private CategoryRepository categoryRepository;

    private CategoryServiceImpl (CategoryRepository categoryRepository) {
        super();
        this.categoryRepository = categoryRepository;
    }

    @Override
    public List<Category> getAllCategory() {
        return categoryRepository.findAll();
    }

}
