package com.inburger.backend.models;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Data
public class OrderDetailDTO {

    int count;
    boolean isSet;
    int price;
    long menu_id;
    List<CustomDTO> customDTO;

    public OrderDetailDTO(int count,
            boolean isSet,
            int price,
            long menu_id,
            List<CustomDTO> customDTO) {
        this.count = count;
        this.isSet = isSet;
        this.menu_id= menu_id;
        this.price = price;
        this.customDTO = customDTO;
    }
}