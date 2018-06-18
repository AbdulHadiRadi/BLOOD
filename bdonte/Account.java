package com.blood.abdul.bdonte;

/**
 * Created by abdul on 3/9/2018.
 */

public class Account {
    private User user;
    private boolean email_confirm;
    private String phoneNumber;
    private String location;

    public Account(boolean email_confirm, String phoneNumber, String location) {
        this.email_confirm = email_confirm;
        this.phoneNumber = phoneNumber;
        this.location = location;
    }

    public Account(boolean email_confirm) {
        this.email_confirm = email_confirm;
    }

    public Account(User user, boolean email_confirm, String phoneNumber, String location) {
        this.user = user;
        this.email_confirm = email_confirm;
        this.phoneNumber = phoneNumber;
        this.location = location;
    }

    public User getUser() {
        return user;
    }

    public boolean isEmail_confirm() {
        return email_confirm;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getLocation() {
        return location;
    }
}
