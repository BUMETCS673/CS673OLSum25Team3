package com.bu.getactivecore.service.activity;

import com.bu.getactivecore.model.Activity;
import com.bu.getactivecore.repository.ActivityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Core logic for managing activities.
 */
@Service
public class ActivityService implements ActivityApi {

    @Autowired
    private ActivityRepository m_activityRepo;


    @Override
    public List<Activity> getAllActivities() {
        return m_activityRepo.findAll();
    }

    @Override
    public List<Activity> getActivityByName(String activityName) {
        return m_activityRepo.findByActivityNameContaining(activityName);
    }
}
