package com.bu.getactivecore.config;

import com.bu.getactivecore.model.Activity;
import com.bu.getactivecore.repository.ActivityRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


@Slf4j
@Configuration
public class LoadDatabase {
    @Bean
    CommandLineRunner demoPreloadData(ActivityRepository activityRepo) {
        return args -> {
            Activity act1 = Activity.builder()
                    .activityName("Rock Climbing")
                    .startTime(System.currentTimeMillis())
                    .build();
            Activity act2 = Activity.builder()
                    .activityName("Yoga")
                    .startTime(System.currentTimeMillis())
                    .build();
            Activity act3 = Activity.builder()
                    .activityName("Running")
                    .startTime(System.currentTimeMillis())
                    .build();

            log.info("Preloading {}", activityRepo.save(act1));
            log.info("Preloading {}", activityRepo.save(act2));
            log.info("Preloading {}", activityRepo.save(act3));
        };
    }
}
