package com.inburger.backend.services.servicesImpl;

import com.inburger.backend.exceptions.ResourceNotFoundException;
import com.inburger.backend.models.Menu;
import com.inburger.backend.repositories.MenuRepository;
import com.inburger.backend.services.MenuService;
import org.springframework.stereotype.Service;

import java.util.List;

import static java.awt.SystemColor.menu;

@Service
public class MenuServiceImpl implements MenuService {

    private MenuRepository menuRepository;

    public MenuServiceImpl(MenuRepository menuRepository) {
        super();
        this.menuRepository = menuRepository;
    }

    @Override
    public List<Menu> getAllMenu() {
        return menuRepository.findAll();
    }

    @Override
    public Menu getMenuDetail(long id) {
        return menuRepository.findById(id).orElseThrow(() ->
                new ResourceNotFoundException("Menu", "id", id));
    }

}
