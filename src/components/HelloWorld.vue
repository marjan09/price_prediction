<template>
  <div>
    <h1>Car Price Prediction</h1>
    <label for="brand">Brand:</label>
    <input type="text" v-model="brand" id="brand" placeholder="Enter brand"><br><br>

    <label for="fuel">Fuel:</label>
    <input type="text" v-model="fuel" id="fuel" placeholder="Enter fuel type"><br><br>

    <label for="gearbox">Gearbox:</label>
    <input type="text" v-model="gearbox" id="gearbox" placeholder="Enter gearbox type"><br><br>

    <label for="year">Year:</label>
    <input type="text" v-model="year" id="year" placeholder="Enter year"><br><br>

    <label for="mileage">Mileage (kms):</label>
    <input type="text" v-model="mileage" id="mileage" placeholder="Enter mileage"><br><br>

    <button @click="predictPrice">Predict Price</button><br><br>

    <p v-if="price">Predicted Price: {{ price }}</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      brand: '',
      fuel: '',
      gearbox: '',
      year: '',
      mileage: '',
      price: null,
      error: null
    }
  },
  methods: {
    async predictPrice() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/predict', {
          params: {
            brand: this.brand,
            fuel: this.fuel,
            gearbox: this.gearbox,
            year: this.year,
            mileage: this.mileage
          }
        });

        if (response.data.error) {
          this.error = response.data.error;
          this.price = null;
        } else {
          this.error = null;
          this.price = response.data.price;
        }
      } catch (error) {
        console.error('Error:', error);
        this.error = 'An error occurred while making the prediction.';
        this.price = null;
      }
    }
  }
}
</script>

<style scoped>
/* CSS styles specific to this component */
</style>