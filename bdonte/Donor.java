package com.blood.abdul.bdonte;


/**
 * Created by abdul on 3/8/2018.
 */

public class Donor {
    private User user;
    private String bloodGroup;
    private String birth_date;
    private String last_donated_date;
    private boolean capable;
    private String gender;


    public Donor(User user, String bloodGroup, String birth_date, String last_donated_date, boolean capable, String gender) {
        this.user = user;
        this.bloodGroup = bloodGroup;
        this.birth_date = birth_date;
        this.last_donated_date = last_donated_date;
        this.capable = capable;
        this.gender = gender;
    }


    public Donor(String bloodGroup, String birth_date, String last_donated_date, boolean capable, String gender) {
        this.bloodGroup = bloodGroup;
        this.birth_date = birth_date;
        this.last_donated_date = last_donated_date;
        this.capable = capable;
        this.gender = gender;
    }

    public User getUser() {
        return user;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public String getBirth_date() {
        return birth_date;
    }

    public String getLast_donated_date() {
        return last_donated_date;
    }

    public boolean isCapable() {
        return capable;
    }

    public String getGender() {
        return gender;
    }
}