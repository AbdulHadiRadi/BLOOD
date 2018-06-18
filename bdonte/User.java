package com.blood.abdul.bdonte;

/**
 * Created by abdul on 3/8/2018.
 */

public class User {
    private String id;
    private String email;
    private String first_name;
    private String last_name;
    protected String password;
    private boolean is_donor;

    public User(String email, String password) {
        this.email = email;
        this.password = password;
    }

    public User(String email, String first_name, String last_name, String password) {
        this.email = email;
        this.first_name = first_name;
        this.last_name = last_name;
        this.password = password;
        this.is_donor = true;
    }

    public User(String id, String email, String first_name, String last_name, boolean is_donor) {
        this.id = id;
        this.email = email;
        this.first_name = first_name;
        this.last_name = last_name;
        this.is_donor = is_donor;
    }

    public String getId() {
        return id;
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public String getEmail() {
        return email;
    }

}