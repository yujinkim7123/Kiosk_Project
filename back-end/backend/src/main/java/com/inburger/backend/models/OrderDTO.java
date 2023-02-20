// 메뉴룰 저장하기 위한 DTO

package com.inburger.backend.models;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Data
public class OrderDTO {

    List<OrderDetailDTO> orderDetailDTO;
    Order order;
    Long user_id;

    public OrderDTO(Order order, Long user_id, List<OrderDetailDTO> orderDetailDTO) {
        this.order = order;
        this.user_id = user_id;
        this.orderDetailDTO = orderDetailDTO;
    }
}
