package com.blood.abdul.bdonte;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class RegisterActivity extends AppCompatActivity  {

    private EditText firstName;
    private EditText lastName;
    private EditText password;
    private EditText email;
    private EditText confirmPass;
    private Api mService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        firstName = (EditText) findViewById(R.id.first_name);
        lastName = (EditText) findViewById(R.id.last_name);
        email = (EditText) findViewById(R.id.email);
        password = (EditText) findViewById(R.id.password);
        confirmPass = (EditText) findViewById(R.id.confirmPass);
        mService = ApiUtils.getSOService();

        Bundle b = getIntent().getExtras();
        String value; // or other values
        if(b != null)
        {
            Intent intent = getIntent();
            String id = b.getString("id");
            String firstName = b.getString("first_name");
            String lastName = b.getString("last_name");
            Log.d(id, "Loggedid");
        }
    }

    public void returnSignIn(View view) {
        Intent intent = new Intent(RegisterActivity.this, SigninActivity.class);
        startActivity(intent);
        finish();
    }

    public void userCreate(View view) throws IOException {
        if(email.getText().toString().isEmpty() || firstName.getText().toString().isEmpty() ||lastName.getText().toString().isEmpty() || password.getText().toString().isEmpty() ){
            Toast.makeText(getApplicationContext(),"Empty field! Try again.",Toast.LENGTH_SHORT).show();
        }
        else{
            if(!password.getText().toString().equals(confirmPass.getText().toString())){
                Toast.makeText(getApplicationContext(),"Password doesn't Match!.",Toast.LENGTH_SHORT).show();
            }
            else if (!isPasswordValid(password.getText().toString())){
                Toast.makeText(getApplicationContext(),"Password less than 8 characters!.",Toast.LENGTH_SHORT).show();
            }
            else if (!isValidEmailAddress(email.getText().toString())) {
                Toast.makeText(getApplicationContext(),"Invalid Email Address!",Toast.LENGTH_SHORT).show();
            }
            else {
                User user = new User(email.getText().toString(), firstName.getText().toString(), lastName.getText().toString(), password.getText().toString());
                registerUser(user);
            }
        }

    }



    private void registerUser(User user) {
        mService = ApiUtils.getSOService();
        mService.CreateUser(user).enqueue(new Callback<User>() {
            @Override
            public void onResponse(Call<User> call, Response<User> response) {

                if(response.isSuccessful()) {
                    User log = new User(email.getText().toString(),password.getText().toString());
                    getID(log);
                }else {
                    Toast.makeText(getApplicationContext(),"Email Address Already Registered!",Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<User> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"Network Problem! Try Again.",Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void getID(User detail) {
            mService.userLogin(detail).enqueue(new Callback<User>() {
                @Override
                public void onResponse(Call<User> call, Response<User> response) {

                    if(response.isSuccessful()) {
                        Intent intent = new Intent(RegisterActivity.this, DonorActivity.class);
                        intent.putExtra("id", response.body().getId().toString());
                        startActivity(intent);
                        finish();
                    }
                }

                @Override
                public void onFailure(Call<User> call, Throwable t) {
                }
            });
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
