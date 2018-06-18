package com.blood.abdul.bdonte;

/**
 * Created by abdul on 3/8/2018.
 */


import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;

/**
 * Created by Belal on 10/2/2017.
 */

public interface Api {

//    String BASE_URL = "http://10.0.2.2:8000/api/";
//    String BASE_URL = "http://138.37.227.175/api/";

    @POST("login/")
    Call<User> userLogin(@Body User detail);


    @POST("changePassword/")
    Call<ChangePassword> changePassword(@Body ChangePassword changePassword);

    @GET("user/")
    Call<List<User>> getUsers();


    @GET("get_accountID/{id}")
    Call<AccountID> getAccountID(@Path("id") String id);

    @GET("get_donorID/{id}")
    Call<DonorID> getDonorID(@Path("id") String id);


    /*  @POST("{id}")
    @FormUrlEncoded
    Call<User> CreateUser(
                        @Path("id") String id,
                        @Field("email") String email,
                        @Field("first_name") String first_name,
                        @Field("last_name") String last_name,
                        @Field("is_donor") boolean is_donor

    );

   */
    @POST("user/")
    Call<User> CreateUser(@Body User user);

    @PUT("account_update/{id}")
    Call<Account> UpdateAccount(@Path("id") String id, @Body Account account);

    @PUT("donor_update/{id}")
    Call<Donor> UpdateDonor(@Path("id") String id, @Body Donor donor);
}