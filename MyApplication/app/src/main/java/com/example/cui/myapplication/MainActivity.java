package com.example.cui.myapplication;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Camera;
import android.graphics.Canvas;
import android.graphics.ColorMatrix;
import android.graphics.ColorMatrixColorFilter;
import android.graphics.Paint;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import org.opencv.android.OpenCVLoader;
import org.opencv.android.Utils;
import org.opencv.core.Mat;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    ImageView imgview;
    Button cambutton;
    static final int REQUEST_IMAGE_CAPTURE = 1;
    private static final String TAG = "MyApp";
    private PreProcessing mImgProcessor = new PreProcessing();

    //Initialize open cv
    static {
        if(OpenCVLoader.initDebug()) {
            Log.d(TAG,"OpenCV Successfully Loaded");
        }
        else {
            Log.d(TAG,"OpenCV Load Not Successfully");
        }
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cambutton = (Button) findViewById(R.id.clickphoto);
        imgview = (ImageView) findViewById(R.id.photodisp);

        cambutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
                    startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
                }
                }
        });

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");
            Bitmap originalBitmap = (Bitmap) extras.get("data");

            Mat imgToProcess = mImgProcessor.preProcessImage(imageBitmap);
            Bitmap.createScaledBitmap(imageBitmap,imgToProcess.width(),imgToProcess.height(),false);
            Bitmap.createScaledBitmap(originalBitmap,imgToProcess.width(),imgToProcess.height(),false);
            Utils.matToBitmap(imgToProcess.clone(),imageBitmap);
            imgview.setImageBitmap(imageBitmap);



        }
    }

    // Greyscale conversion shifted to PreProcessing file
    /*
    public Bitmap toGrayscale(Bitmap bmpOriginal)
    {
        int width, height;
        height = bmpOriginal.getHeight();
        width = bmpOriginal.getWidth();

        Bitmap bmpGrayscale = Bitmap.createBitmap(width, height, Bitmap.Config.RGB_565);
        Canvas c = new Canvas(bmpGrayscale);
        Paint paint = new Paint();
        ColorMatrix cm = new ColorMatrix();
        cm.setSaturation(0);
        ColorMatrixColorFilter f = new ColorMatrixColorFilter(cm);
        paint.setColorFilter(f);
        c.drawBitmap(bmpOriginal, 0, 0, paint);
        return bmpGrayscale;
    }

    */


}
