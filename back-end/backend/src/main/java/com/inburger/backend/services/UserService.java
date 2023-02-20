package com.inburger.backend.services;

import com.inburger.backend.models.User;

import java.util.List;

public interface UserService {

    List<User> getAllUser();
    User saveUser(User user);
    void deleteUserById(long id);
    User getUserById(long id);
}
