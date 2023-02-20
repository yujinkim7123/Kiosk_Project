package com.inburger.backend.models;

import javax.persistence.*;

import com.fasterxml.jackson.annotation.JsonBackReference;
import lombok.*;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "TABLE_CUSTOM")
@Builder
public class Custom {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "custom_id")
    private Long id;

    @Column(name = "ingredient_count")
    private int count;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference //추가
    @JoinColumn(name = "ingredient_id", nullable = false)
    private Ingredient ingredient;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference //추가
    @JoinColumn(name = "order_detail_id", nullable = true, updatable = true)
    private OrderDetail orderDetail;
}



