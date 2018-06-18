package com.blood.abdul.bdonte;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Reset_PasswordActivity extends AppCompatActivity {

    private EditText password;
    private EditText email;
    private EditText confirmPass;
    private Api mService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reset__password);
        email = (EditText) findViewById(R.id.email);
        password = (EditText) findViewById(R.id.password);
        confirmPass = (EditText) findViewById(R.id.confirmPass);
        mService = ApiUtils.getSOService();
    }

    public void resetPassword(View view) {
        if(email.getText().toString().isEmpty() || password.getText().toString().isEmpty() ){
            Toast.makeText(getApplicationContext(),"Empty field! Try again.",Toast.LENGTH_SHORT).show();
        }
        else{
            if (!isValidEmailAddress(email.getText().toString())) {
            Toast.makeText(getApplicationContext(),"Invalid Email Address!",Toast.LENGTH_SHORT).show();
            }

            else if(password.getText().toString().equals(confirmPass.getText().toString())){
                Toast.makeText(getApplicationContext(),"Old password matched! Please use new Password.",Toast.LENGTH_SHORT).show();
            }

            else if (!isPasswordValid(confirmPass.getText().toString())){
                Toast.makeText(getApplicationContext(),"Password less than 8 characters!.",Toast.LENGTH_SHORT).show();
            }
            else{
                changePassword(password.getText().toString(), confirmPass.getText().toString());
            }
        }
    }

    private void changePassword(String oldPass, String newPass) {
        ChangePassword change = new ChangePassword(oldPass, newPass);
        mService = ApiUtils.getSOService();
        mService.changePassword(change).enqueue(new Callback<ChangePassword>() {
            @Override
            public void onResponse(Call<ChangePassword> call, Response<ChangePassword> response) {

                if(response.isSuccessful()) {
                    Intent intent = new Intent(Reset_PasswordActivity.this, SigninActivity.class);
                    startActivity(intent);
                    finish();
                }else {
                    Toast.makeText(getApplicationContext(),"Wrong Credentials is given! Try Again",Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<ChangePassword> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"Wrong Credentials is given! Try Again.",Toast.LENGTH_SHORT).show();
            }
        });
    }


    public void cancelReset(View view) {
        Intent intent = new Intent(Reset_PasswordActivity.this, SigninActivity.class);
        startActivity(intent);
        finish();
    }
    //registration password length
    private boolean isPasswordValid(String password) {
        //TODO: Replace this with your own logic
        return password.length() >= 8;
    }

    public static boolean isValidEmailAddress(String email) {
        return email.contains("@");
    }
}


