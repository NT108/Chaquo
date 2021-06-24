package com.nisarg.chaquo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button btn1;
    Spinner spn1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn1 = (Button) findViewById(R.id.button);
        spn1 = (Spinner) findViewById(R.id.spinner);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(spn1.getSelectedItemPosition() == 0){
                    Toast.makeText(MainActivity.this, "You need to select a username to view data", Toast.LENGTH_SHORT).show();
                }
                else{


                Intent i = new Intent(MainActivity.this, analysis.class);
                i.putExtra("Username", spn1.getSelectedItem().toString());
                startActivity(i);

            }}
        });

    }
}