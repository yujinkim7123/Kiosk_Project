package com.inburger.backend.controllers;

import com.inburger.backend.models.User;
import com.inburger.backend.repositories.UserRepository;
import com.inburger.backend.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/inburger")

@CrossOrigin("http://3.36.49.220:3000/")

public class UserController {

    private UserService userService;
    private final UserRepository userRepository;

    @Autowired
    public UserController(UserRepository userRepository,
                          UserService userService){
        this.userRepository = userRepository;
        this.userService = userService;
    }

    // 모든 유저 정보 조회
    @GetMapping(value = "/user")
    public List<User> getAllUser(){
        return userService.getAllUser();
    }

    // 유저 정보 저장
    @PostMapping(value = "/user", produces = "application/json;charset=UTF-8")
    public User saveUser(@RequestBody User user) {
        if (user.getName() == "none"){
            return null;
        }
        else {
            return userService.saveUser(user);
        }
    }

    // 유저 정보 삭제
    @DeleteMapping(value = "/user/{id}")
    public void deleteUser(@PathVariable("id") Long id){
        userService.deleteUserById(id);
    }

}
