package com.blood.abdul.bdonte;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class DonorActivity extends AppCompatActivity {
    private String id;
    private String accID;
    private String donID;
    private EditText firstName;
    private EditText lastName;
    private EditText password;
    private EditText email;
    private EditText confirmPass;
    private Api mService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_donor);
        mService = ApiUtils.getSOService();

        Bundle b = getIntent().getExtras();
        String value; // or other values
        if(b != null)
        {
            Intent intent = getIntent();
            id = b.getString("id");
            Log.d(id, "id");
        }
    }


    public void returnSignIn(View view) {
        Intent intent = new Intent(DonorActivity.this, SigninActivity.class);
        startActivity(intent);
        finish();
    }

    public void createAccount(View view) {
//        Intent intent = new Intent(DonorActivity.this, RegisterActivity.class);
//        startActivity(intent);
//        finish();
        getAccountID(id);
        getDonorID(id);
        Toast.makeText(getApplicationContext(),"Yes.",Toast.LENGTH_SHORT).show();
    }

    private void getAccountID(String id) {
        mService = ApiUtils.getSOService();
        mService.getAccountID(id).enqueue(new Callback<AccountID>() {
            @Override
            public void onResponse(Call<AccountID> call, Response<AccountID> response) {

                if(response.isSuccessful()) {
                    accID = response.body().getAccID().toString();
                    Log.d("Accid", response.body().getAccID().toString());
                }
            }

            @Override
            public void onFailure(Call<AccountID> call, Throwable t) {
            }
        });
    }

    private void getDonorID(String id) {
        mService = ApiUtils.getSOService();
        mService.getDonorID(id).enqueue(new Callback<DonorID>() {
            @Override
            public void onResponse(Call<DonorID> call, Response<DonorID> response) {

                if(response.isSuccessful()) {
                    donID = response.body().getAccID().toString();
                    Log.d("donid", response.body().getAccID().toString());
                }
            }

            @Override
            public void onFailure(Call<DonorID> call, Throwable t) {
            }
        });
    }
}
