package com.blood.abdul.bdonte;

/**
 * Created by abdul on 4/6/2018.
 */

public class ApiUtils {

  public static final String BASE_URL = "http://10.0.2.2:8000/api/";
    //String BASE_URL = "http://138.37.227.175/api/";

    public static Api getSOService() {
        return RetrofitClient.getClient(BASE_URL).create(Api.class);
    }
}