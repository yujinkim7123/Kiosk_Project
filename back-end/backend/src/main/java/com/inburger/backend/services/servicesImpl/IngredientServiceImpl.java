package com.inburger.backend.services.servicesImpl;

import com.inburger.backend.models.Ingredient;
import com.inburger.backend.repositories.IngredientRepository;
import com.inburger.backend.services.IngredientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class IngredientServiceImpl implements IngredientService {

    private IngredientRepository ingredientRepository;

    public IngredientServiceImpl(IngredientRepository ingredientRepository) {
        super();
        this.ingredientRepository = ingredientRepository;
    }


    @Override
    public List<Ingredient> getAllIngredient() {
        return ingredientRepository.findAll();
    }
}

