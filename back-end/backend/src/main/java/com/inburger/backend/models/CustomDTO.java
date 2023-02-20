package com.inburger.backend.models;

import lombok.Builder;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;


@Getter
@Setter
@Data
@Builder

public class CustomDTO {

    String ingredientName;
    int ingredientCount;

    public CustomDTO(String ingredientName, int ingredientCount) {
        this.ingredientName = ingredientName;
        this.ingredientCount = ingredientCount;
    }
}
