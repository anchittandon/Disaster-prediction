package com.example.abhishek.codefundo;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.TextView;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    LocationManager locationManager;
    LocationListener locationListener;

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater menuInflater=getMenuInflater();
        menuInflater.inflate(R.menu.main_menu,menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if(item.getItemId()==R.id.map){
            Intent intent=new Intent(getApplicationContext(),MapsActivity.class);
            startActivity(intent);
            return true;
        }
        return false;
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if(grantResults.length>0 &&grantResults[0]==PackageManager.PERMISSION_GRANTED){

            if(ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)== PackageManager.PERMISSION_GRANTED){

                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,0,locationListener);

            }

        }
    }

    public void updateLocationInfo(Location location){
        Log.i("Location Info ",location.toString());
        TextView latTextView=(TextView)findViewById(R.id.latTextView);
        TextView lngtTextView=(TextView)findViewById(R.id.lngTextView);
        TextView altTextView=(TextView)findViewById(R.id.altTextView);
        TextView accTextView=(TextView)findViewById(R.id.accTextView);

        latTextView.setText("Latitude: "+String.valueOf(location.getLatitude()));
        lngtTextView.setText("Longitude: "+String.valueOf(location.getLongitude()));
        altTextView.setText("Altitude: "+String.valueOf(location.getAltitude()));
        accTextView.setText("Accuracy: "+String.valueOf(location.getAccuracy()));

        Geocoder geocoder=new Geocoder(getApplicationContext(), Locale.getDefault());
        try {

            String address="Could not find address";
            List<Address> listAddress=geocoder.getFromLocation(location.getLatitude(),location.getLongitude(),1);

            if(listAddress!=null &&listAddress.size()>0 ){
                Log.i("PLaceInfo", listAddress.get(0).toString());
                address="";
                if(listAddress.get(0).getSubThoroughfare()!=null){
                    address+=listAddress.get(0).getSubThoroughfare()+"\n";
                }
                if(listAddress.get(0).getThoroughfare()!=null){
                    address+=listAddress.get(0).getThoroughfare()+"\n";
                }
                if(listAddress.get(0).getLocality()!=null){
                    address+=listAddress.get(0).getLocality()+"\n";
                }
                if(listAddress.get(0).getPostalCode()!=null){
                    address+=listAddress.get(0).getPostalCode()+"\n";
                }
                if(listAddress.get(0).getAdminArea()!= null){
                    address+=listAddress.get(0).getAdminArea()+"\n";
                }
                if(listAddress.get(0).getCountryName()!=null){
                    address+=listAddress.get(0).getCountryName()+".";
                }
                TextView addTextView=(TextView)findViewById(R.id.addTextView);
                addTextView.setText("Address:\n "+address);

            }
        } catch (IOException e) {
            e.printStackTrace();
        }


    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        locationManager=(LocationManager)this.getSystemService(Context.LOCATION_SERVICE);
        locationListener=new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                Log.i("Location ",location.toString());
                updateLocationInfo(location);
            }

            @Override
            public void onStatusChanged(String provider, int status, Bundle extras) {

            }

            @Override
            public void onProviderEnabled(String provider) {

            }

            @Override
            public void onProviderDisabled(String provider) {

            }
        };


        if(ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this,new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1);
        } else{
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,0,locationListener);

            Location location=locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            if(location!=null){
                updateLocationInfo(location);
            }

        }

    }
}
