package com.inburger.backend;

import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.task.TaskExecutor;

@SpringBootApplication
@RequiredArgsConstructor
public class BackendApplication{

//	private final CategoryRepository categoryRepository;
//	private final IngredientRepository ingredientRepository;

	public static void main(String[] args) {

		SpringApplication.run(BackendApplication.class, args);


	}

//	@Override
//	public void run(String... args) throws Exception {

//		// 카테고리 생성
//		if (!categoryRepository.findById(1L).isPresent()) {
//			Category category1 = categoryRepository.save(Category.builder()
//					.name("hamburger")
//					.build());
//			Category category2 = categoryRepository.save(Category.builder()
//					.name("sidemenu")
//					.build());
//			Category category3 = categoryRepository.save(Category.builder()
//					.name("beverage")
//					.build());
//			Category category4 = categoryRepository.save(Category.builder()
//					.name("vegetable")
//					.build());
//			Category category5 = categoryRepository.save(Category.builder()
//					.name("pattie")
//					.build());
//			Category category6 = categoryRepository.save(Category.builder()
//					.name("bread")
//					.build());
//		}
//
//
//		// 재료 설정 생성
//		if (!ingredientRepository.findById(1L).isPresent()) {
//			Ingredient ingredient1 = ingredientRepository.save(Ingredient.builder()
//					.name("bread1")
//					.price(500)
//					.build());
//		}
//	}
}

