package com.bu.getactivecore.service.activity;

import com.bu.getactivecore.model.Activity;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Collections;
import java.util.List;

import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;


@RunWith(SpringRunner.class)
@WebMvcTest(ActivityController.class)
@AutoConfigureMockMvc
class ActivityRestControllerTest {

    @Autowired
    private MockMvc m_mvc;


    @MockitoBean
    private ActivityService m_activityService;

    @Autowired
    private ActivityApi m_activityApi;

    @Test
    public void givenActivities_expectedActivitiesReturned() throws Exception {

        List<Activity> mockedActivities = List.of(
                Activity.builder().activityName("Running").startTime(System.currentTimeMillis()).build(),
                Activity.builder().activityName("Yoga").startTime(System.currentTimeMillis()).build(),
                Activity.builder().activityName("Rock Climbing").startTime(System.currentTimeMillis()).build()
        );
        given(m_activityApi.getAllActivities()).willReturn(mockedActivities);
        m_mvc.perform(
                        get("/v1/activities").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].activityName").value("Running"))
                .andExpect(jsonPath("$[1].activityName").value("Yoga"))
                .andExpect(jsonPath("$[2].activityName").value("Rock Climbing"));


    }

    @Test
    public void givenNoActivities_then_200Returned() throws Exception {

        List<Activity> mockedActivities = Collections.emptyList();
        given(m_activityApi.getAllActivities()).willReturn(mockedActivities);
        m_mvc.perform(
                        get("/v1/activities").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$").isEmpty());
    }
}