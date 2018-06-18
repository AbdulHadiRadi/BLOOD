package com.blood.abdul.bdonte;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.Toast;

import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class SigninActivity extends AppCompatActivity {
    private AutoCompleteTextView mEmailView;
    private EditText mPasswordView;
    private Api mService;
    String SenderID = "1521899512641";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signin);
        mEmailView = (AutoCompleteTextView) findViewById(R.id.email);
        mPasswordView = (EditText) findViewById(R.id.password);
        mService = ApiUtils.getSOService();
    }

    public void register(View view) {
        Intent intent = new Intent(SigninActivity.this, RegisterActivity.class);
        startActivity(intent);
        finish();
    }


    public void signIn(View view) throws IOException {
        if(mEmailView.getText().toString().isEmpty() || mPasswordView.getText().toString().isEmpty()) {
            Toast.makeText(getApplicationContext(),"Empty field! Try Again.",Toast.LENGTH_SHORT).show();
        }
        else{
            User detail = new User(mEmailView.getText().toString(), mPasswordView.getText().toString());
            loadAnswers(detail);
        }
    }

    public void loadAnswers(User detail) {
        mService.userLogin(detail).enqueue(new Callback<User>() {
            @Override
            public void onResponse(Call<User> call, Response<User> response) {

                if(response.isSuccessful()) {
                    Toast.makeText(getApplicationContext(),"Logged In Successfully to BDonate!",Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(SigninActivity.this, DonorActivity.class);
                    intent.putExtra("id", response.body().getId().toString());
                    intent.putExtra("first_name", response.body().getFirst_name().toString());
                    intent.putExtra("last_name", response.body().getLast_name().toString());
                    Log.d("id", response.body().getId().toString());
                    startActivity(intent);
                    finish();
                }else {
                    Toast.makeText(getApplicationContext(),"Wrong Credentials! Try Again.",Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<User> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"Network Problem! Try Again.",Toast.LENGTH_SHORT).show();
            }
        });
    }

    public void resetPassword(View view) {
        if(mEmailView.getText().toString().isEmpty()){
            Toast.makeText(getApplicationContext(),"Fill the email field first!",Toast.LENGTH_SHORT).show();
        }
        else{
            Intent intent = new Intent(SigninActivity.this, RegisterActivity.class);
            startActivity(intent);
            finish();
        }
    }
}


