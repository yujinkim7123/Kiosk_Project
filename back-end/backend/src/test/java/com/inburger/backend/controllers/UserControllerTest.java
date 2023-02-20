package com.inburger.backend.controllers;

import com.inburger.backend.BackendApplicationTests;
import com.inburger.backend.models.User;
import com.inburger.backend.repositories.UserRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class UserControllerTest extends BackendApplicationTests {
    @Autowired
    private UserRepository userRepository;

    @AfterEach
    public void cleanUp() {
        userRepository.deleteAll();
    }

    @Test
    void createUser() {
        User user1 = new User();
        user1.setName("A1");
        user1.setIsEasy(1);
        user1.setHeight(1);

        //when
        User user = userRepository.save(user1);

        //then
        assertSame(user, user1);
    }

    @Test
    void getAllUsers() {
        String name = "A1";
        int age = 20;
        int height = 1;

        User user1 = new User();
        user1.setName(name);
        user1.setIsEasy(age);
        user1.setHeight(height);
        userRepository.save(user1);

        //when
        List<User> userList = userRepository.findAll();

        //then
        User user = userList.get(0);
        assertEquals(name, user.getName());
        assertEquals(age, user.getIsEasy());
        assertEquals(height, user.getHeight());
    }
}