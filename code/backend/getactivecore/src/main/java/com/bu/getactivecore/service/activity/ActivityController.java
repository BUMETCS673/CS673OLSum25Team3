package com.bu.getactivecore.service.activity;

import com.bu.getactivecore.model.Activity;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.HashMap;
import java.util.Map;

/**
 * Entry point for all activity-related APIs.
 */
@Slf4j
@RestController
@RequestMapping("/v1")
@CrossOrigin(origins = "*")
public class ActivityController {

    @Autowired
    private ActivityApi m_activityApi;

    /**
     * Get all activities.
     *
     * @return List of activities
     */
    @GetMapping("/activities")
    public List<Activity> getActivities() {
        log.info("Got request: /v1/activities");
        return m_activityApi.getAllActivities();
    }

    /**
     * Get activities by name.
     *
     * @param activityName Name of the activity
     * @return List of activities matching the name
     */
    @GetMapping("/activity/{activityName}")
    public List<Activity> getActivityByName(@PathVariable String activityName) {
        log.info("Got request: /v1/activity/{}", activityName);
        return m_activityApi.getActivityByName(activityName);
    }

    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> healthCheck() {
        Map<String, String> response = new HashMap<>();
        response.put("status", "UP");
        response.put("message", "Service is running");
        response.put("timestamp", String.valueOf(System.currentTimeMillis()));
        
        return ResponseEntity.ok(response);
    }
}
