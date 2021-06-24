package com.nisarg.chaquo;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class analysis extends AppCompatActivity {
    ImageView iv1;
    Intent i ;
    String Username;
    byte[] framedata;
    Python py;
    PyObject pyobj;
    PyObject obj;

    @Override
    public void onBackPressed() {
        finish();


    } // on back pressed





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_analysis);
        iv1 = (ImageView) findViewById(R.id.imageView);
        iv1.setImageDrawable(null);


        if(!Python.isStarted())
            Python.start(new AndroidPlatform(this));

        i = getIntent();

        Username = i.getStringExtra("Username");
        Toast.makeText(this, Username, Toast.LENGTH_SHORT).show();


        py = Python.getInstance();
        pyobj = py.getModule("Highest Selling Product");


                 obj = pyobj.callAttr("indicidulUserGraph", Username);

                framedata = py.getBuiltins().callAttr("bytes", obj).toJava(byte[].class);
                Bitmap bitmap = BitmapFactory.decodeByteArray(framedata, 0, framedata.length);
                iv1.setImageBitmap(bitmap);





    }
}