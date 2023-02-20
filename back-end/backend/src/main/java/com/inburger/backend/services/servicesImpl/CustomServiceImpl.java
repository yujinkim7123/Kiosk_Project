package com.inburger.backend.services.servicesImpl;

import com.inburger.backend.exceptions.ResourceNotFoundException;
import com.inburger.backend.models.Category;
import com.inburger.backend.models.Custom;
import com.inburger.backend.models.Ingredient;
import com.inburger.backend.models.OrderDetail;
import com.inburger.backend.repositories.CategoryRepository;
import com.inburger.backend.repositories.CustomRepository;
import com.inburger.backend.repositories.IngredientRepository;
import com.inburger.backend.repositories.OrderDetailRepository;
import com.inburger.backend.services.CustomService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CustomServiceImpl implements CustomService {

    private CustomRepository customRepository;
    private CategoryRepository categoryRepository;
    private IngredientRepository ingredientRepository;
    private OrderDetailRepository orderDetailRepository;

    private CustomServiceImpl(CustomRepository customRepository,
                              CategoryRepository categoryRepository,
                              IngredientRepository ingredientRepository,
                              OrderDetailRepository orderDetailRepository) {
        super();
        this.customRepository = customRepository;
        this.categoryRepository = categoryRepository;
        this.ingredientRepository = ingredientRepository;
        this.orderDetailRepository = orderDetailRepository;
    }
    @Override
    public List<Custom> getAllCustom() {
        return customRepository.findAll();
    }

    @Override
    public Custom saveCustom(String ingredientName, int count, long orderDetailId) {
        System.out.println(ingredientRepository.findByName(ingredientName));
        Ingredient ingredient = ingredientRepository.findByName(ingredientName);
//        Ingredient ingredient = ingredientRepository.findById(ingredient_id).orElseThrow(() ->
//                new ResourceNotFoundException("category", "category_id", ingredient_id));
        OrderDetail orderdetail = orderDetailRepository.findById(orderDetailId).orElseThrow(() ->
                new ResourceNotFoundException("OrderDetail", "orderDetailId", orderDetailId));
        Custom newCustom = Custom.builder()
                .ingredient(ingredient)
                .orderDetail(orderdetail)
                .count(count)
                .build();
        customRepository.save(newCustom);
        return newCustom;
    }

}
