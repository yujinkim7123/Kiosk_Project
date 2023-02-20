package com.inburger.backend.controllers;

import com.inburger.backend.models.Custom;
import com.inburger.backend.repositories.CustomRepository;
import com.inburger.backend.services.CustomService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(path = "/inburger")
public class CustomController {

    private CustomService customService;
    private final CustomRepository customRepository;

    @Autowired
    public CustomController(CustomRepository customRepository,
                            CustomService customService) {
        this.customRepository = customRepository;
        this.customService = customService;
    }

    @GetMapping(value="/customs")
    public List<Custom> getAllCustom(){
        return customService.getAllCustom();
    }

}
