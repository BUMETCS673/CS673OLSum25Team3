package com.bu.getactivecore.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.UuidGenerator;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity(name = "activity")
@Table(name = "activity")
public class Activity {
    @Id
    @UuidGenerator
    @Column(name = "activity_id")
    private String activityId;

    @Column(name = "activity_name")
    private String activityName;

    @Column(name = "start_time")
    private Long startTime;
}
