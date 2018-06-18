package com.blood.abdul.bdonte;

/**
 * Created by abdul on 3/19/2018.
 */

public class DonorID {
    private String id;
    private String accID;

    public DonorID(String id, String accID) {
        this.id = id;
        this.accID = accID;
    }

    public String getId() {
        return id;
    }

    public String getAccID() {
        return accID;
    }
}
