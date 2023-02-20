package com.inburger.backend.models;

import javax.persistence.*;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "TABLE_ORDER_DETAIL")
@Builder
public class OrderDetail {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "menu_count", nullable = false)
    private Integer count;

    @Column(name = "each_menu_price", nullable = false)
    private Integer price;

    @Column(name = "is_set", nullable = true)
    private Boolean is_set;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id")
    @JsonBackReference
    private Order order;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "menu_id")
    @JsonBackReference
    private Menu menu;

    @JsonManagedReference
    @OneToMany(mappedBy = "orderDetail", cascade = CascadeType.ALL)
    private List<Custom> customs = new ArrayList<>();

}


