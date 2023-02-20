package com.inburger.backend.models;

import lombok.Builder;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.List;


@Getter
@Setter
@Data
@Builder
public class MenuDTO {

    String menuName;
    List<CustomDTO> menuCustomDTO;
    Integer customPrice;

    public MenuDTO(String menuName, List<CustomDTO> menuCustomDTO, Integer customPrice) {
        this.menuName = menuName;
        this.menuCustomDTO = menuCustomDTO;
        this.customPrice = customPrice;
    }
}
