/*////////////////////////////////////////////////////////////////////////////////////////////////////////
// Olivia Spears																						//
// CWID: 10240548																						//
// CSC 475 - Assignment 2																				//
// Due: 10.19.2018 @ 9:00 am																			//
// A neural network that can be trained to recognize handwritten numbers.								//
// A BIG HEADS UP! The training and testing data paths need to be in the same directory	:0				//
// The paths are set at the beginning of the NeuralNetwork class if you don't want to move your data	//
////////////////////////////////////////////////////////////////////////////////////////////////////////*/
 
// the import statements!!!!!!! :o
import java.util.Scanner;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

import java.lang.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;

import java.text.DecimalFormat;

// The main function for handling everything else.
class NeuralNetwork {	
	// The locations of the MNIST training data and testing data
	public static String training_data = "mnist_train.csv";
	public static String test_data = "mnist_test.csv";

	// Handles the user wanting to work with a fresh network from Scratch
	public static void train () {
		// If its a new network it needs the random weights and biases
		Network network = new Network();
		network.initialsetup();
		while(true) {
			System.out.println("\nWhat are we doing today?\n[1] Train network.\n[2] Display network accuracy over TRAINING data.\n[3] Display network accuracy over TESTING data.\n[4] Save the current weights and biases. \n[5] Go back");
			Scanner read = new Scanner(System.in);
			int n = read.nextInt();
			if (n == 1) {
				// train it with the MNIST training data
				network.stochastic_gradient_descent(training_data);
			} else if (n == 2) {
				// test network with training data. no training
				network.feedforward(training_data, false);
			} else if (n == 3) {
				// test network with test data. no training
				network.feedforward(test_data, true);
			} else if (n == 4) {
				// Saving the networks current weights and biases
				try {
					System.out.println("Please name the file");
					String name = read.next();
					network.Save(name);
				} catch (IOException e) {
					System.out.println(e);
				}
			} else if (n == 5) {
				// back to main
				System.out.println("Back to main page");		
				break;
			} else {
				System.out.println("Whoops!! That's not a correct command!");
			}
		}
	}
	
	// Handles the user wanting to first load an old network
	public static void load () {
		// initialize a new network and then be ready to LOAD IN SOME WEIGHTS
		Network network = new Network();
		System.out.println("Please give the path to the file you are loading");
		Scanner read = new Scanner(System.in);
		String file = read.next();
		// Attempts to load the requested weights and biases. If it fails it just goes back
		try {
			network.Load(file);
		} catch (IOException e) {
			System.out.println("oops something went wrong!");
            e.printStackTrace();
			return;
        }
		System.out.println("File loaded!");
		while(true) {
			System.out.println("\nWhat are we doing today?\n[1] Train network.\n[2] Display network accuracy over TRAINING data.\n[3] Display network accuracy over TESTING data.\n[4] Save the current weights and biases. \n[5] Go back");
			read = new Scanner(System.in);
			int n = read.nextInt();
			if (n == 1) {
				// train it with the MNIST training data
				network.stochastic_gradient_descent(training_data);
			} else if (n == 2) {
				// test network with training data. no training
				network.feedforward(training_data, false);
			} else if (n == 3) {
				// test network with test data. no training
				network.feedforward(test_data, true);
			} else if (n == 4) {
				// Saving the networks current weights and biases
				try {
					System.out.println("Please name the file");
					String name = read.next();
					network.Save(name);
				} catch (IOException e) {
					System.out.println(e);
				}
			} else if (n == 5) {
				// back to main
				System.out.println("Back to main page");		
				break;
			} else {
				System.out.println("Whoops!! That's not a correct command!");
			}
		}
	}
	
	// Main function
	public static void main (String args[]) {
		/* This is the main function. I'm using this as a nice lil command line home base */
		Scanner read = new Scanner(System.in);
		System.out.println(".*.*.*.*. Welcome to Olivia's Superb Neural Network!!!! .*.*.*.*.");
		
		while (true) {
			System.out.println("\nPlease make a selection.\n[1] Train a new network\n[2] Load a previously trained network\n[3] Quit");
			int n = read.nextInt();
			if (n == 1) {
				// Go work with a new network
				NeuralNetwork.train();
			} else if (n == 2) {
				// Work with an old network
				NeuralNetwork.load();
			} else if (n == 3) {
				// Exit
				System.out.println("Thank you! Goodbye :)");
				System.exit(0);
			} else {
				System.out.println("Whoops!! That's not a correct command!");
			}
		}
	}
	
 }
 
// Holds the network's methods and weights and biases and allll the good stuff
class Network {
	// Weights and biases
	public float[][] weight1 = new float[30][784];
	public float[][] weight2 = new float[10][30];
	public float[] bias1 = new float[30];
	public float[] bias2 = new float[10];
	// stuff for learning in an EZ to change location
	private float learning_rate = 3.0f;
	private int batch_size = 10;
	private int epochs = 30;
	
	// Constructor for the network
	public Network() {

	}
	
	//Used to save the weights and biases
	public void Save(String fileName) throws IOException {
		// formats the decimals... I was having issues with scientific notation
		DecimalFormat df = new DecimalFormat("#.####");
		// if the filename was inputed as just a string 
		if (!fileName.contains(".csv")) {
			fileName = fileName + ".csv";
		}
		System.out.println("saving the data to " + fileName);
		FileWriter writer = new FileWriter(fileName);
        StringBuilder sb = new StringBuilder();
		
		// goes through each weight and bias and puts them in their own respective lines
        for(int j = 0; j < weight1.length; j++) {
			for(int k = 0; k < weight1[0].length; k++) {
				sb.append(df.format(weight1[j][k]));
				if(j != weight1.length-1) {
					sb.append(",");
				} else if (j == weight1.length-1) {
					if(k != weight1[0].length-1) {
						sb.append(",");						
					}
				} 
			}
		}
		sb.append(System.lineSeparator());
		for(int k = 0; k < bias1.length; k++) {
			sb.append(df.format(bias1[k]));
			if(k != bias1.length-1) {
				sb.append(",");
			}
		}
		sb.append(System.lineSeparator());		
		for(int j = 0; j < weight2.length; j++) {
			for(int k = 0; k < weight2[0].length; k++) {
				sb.append(df.format(weight2[j][k]));
				if(j != weight2.length-1) {
					sb.append(",");
				} else if (j == weight2.length-1) {
					if(k != weight2[0].length-1) {
						sb.append(",");						
					}
				} 
			}
		}
		sb.append(System.lineSeparator());
		for(int k = 0; k < bias2.length; k++) {
			sb.append(df.format(bias2[k]));
			if(k != bias2.length-1) {
				sb.append(",");
			}
		}
		
		// Adds the big ol string to the filewriter, writes the file, and closes the writer :-)
        writer.append(sb.toString());
        writer.close();
	}
	
	//Used to load weights and biases
	public void Load(String fileName) throws IOException {
		System.out.println("Loading weights and biases");
		
		// setting up the reader
		String csvFile = fileName;
        String line = "";
        String cvsSplitBy = ",";
		// n is to show which line we're reading. I have it set up to save 4 lines. 2 for the 2 weight layers and 2 for the 2 bias layers
		int n = 1;

        BufferedReader br = new BufferedReader(new FileReader(csvFile));

		while ((line = br.readLine()) != null) {
			int next = 0;
			String[] inputs = line.split(cvsSplitBy);
			// use comma as separator
			switch (n) {
				case 1: //line 1 : weight 1
					for (int j = 0; j < weight1.length; j++) {
						for (int k = 0; k < weight1[0].length; k++) {	
							weight1[j][k] = Float.valueOf(inputs[next]);
							next++;
						}
					}
					break;
					
				case 2: //line 2 : bias 1
					for (int j = 0; j < bias1.length; j++) {
						bias1[j] = Float.valueOf(inputs[j]);
					}
					break;
					
				case 3: //line 3 : weight 2
					for (int j = 0; j < weight2.length; j++) {
						for (int k = 0; k < weight2[0].length; k++) {
							weight2[j][k] = Float.valueOf(inputs[next]);
							next++;
						}
					}
					break;
					
				case 4: //line 4 : bias 2
					for (int j = 0; j < bias2.length; j++) {
						bias2[j] = Float.valueOf(inputs[j]);
					}
					break;
			}
			n++;

		}	
	}
	
	// Used to read the training OR testing data
	public Pair[] getTrainingData(String location, int length) {
		System.out.println("Reading data...");
		// set up reader
		String csvFile = location;
        String line = "";
        String cvsSplitBy = ",";
		// Setting up the results to return. Length is either 60000 or 10000 depending on test or train
		Pair[] result = new Pair[length];

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
			int next_index = 0; // keeping the indexes in line for the results
            while ((line = br.readLine()) != null) {
				String[] inputs = line.split(cvsSplitBy);
				float[] x = new float[784];
				float[] y = new float[10];
				
				// gets the correct answer value for the inputs
				int value = Integer.parseInt(inputs[0]);
				// goes through the new y vector and sets everything to 0 except for the index that corresponds to the correct value of the input
				for(int j = 0; j < y.length; j++) {
					float y_value = (value == j) ? 1f : 0f;
					y[j] = y_value;
				}
				// starting at the second item in the data set, goes through new x vector and sets value to the normalized value of the data
				for(int k = 1; k < x.length + 1; k++) {
					float val = Float.valueOf(inputs[k]) / 255;
					x[k-1] = val; // k-1 bc we start at 1
				}
				result[next_index] = new Pair(x, y); // creating the x,y tuples for the data and then adding to results
				next_index++;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }	
		return result;
	}
	
	// Used to randomize weights and biases for brand new network
	public void initialsetup() {
		System.out.println("\nRandomizing weights and biases...");
		Random r = new Random();
		// goes throught both weights and biases just setting each index to a random float between -1 and 1.
		for(int j = 0; j < weight1.length; j++) { // should be 30
			for(int k = 0; k < weight1[0].length; k++){ // should be 784
				float random = -1 + r.nextFloat() * (1 - (-1));
				weight1[j][k] = random;
			} 
			float random = -1 + r.nextFloat() * (1 - (-1));
			bias1[j] = random;
		}
		
		for(int j = 0; j < weight2.length; j++) { // should be 30
			for(int k = 0; k < weight2[0].length; k++){ // should be 784
				float random = -1 + r.nextFloat() * (1 - (-1));
				weight2[j][k] = random;
			} 
			float random = -1 + r.nextFloat() * (1 - (-1));
			bias2[j] = random;
		}
	}
	
	// A different instance of the method to deal with when its Not called after training.
	public void feedforward(String location, boolean test) {
		int length = test ? 10000 : 60000;
		Pair[] data = getTrainingData(location, length);
		feedforward(data);
	}
	
	// Tests the data with the weights and then processes results. Does not train data.
	public void feedforward(Pair[] input) {
		// A results matrix. The first row is for everytime the guess is correct and the second is for every time a number is tested. Each column represents each number
		int[][] results = new int[2][10];
		// Goes through input and calculates the network's guess
		for (int i = 0; i < input.length; i++) {
			float[] a = input[i].getZ();
			float[] y = input[i].getY();
			float[] z = vector_add((vector_mult(weight1, a, 0f)), bias1);
			a = sigmoid(z);
			z = vector_add(vector_mult(weight2, a, 0f), bias2);
			a = sigmoid(z); // This is the network's outputs for the 10 nodes
			
			int a_val = 0; // the network's guess
			int y_val = 0; // the correct answer
			
			for (int j = 0; j < a.length; j++) {
				// setting the answer of a to the highest valued output
				if (a[j] > (float) a[a_val]) {
					a_val = j;
				}
				// getting the int of what y is 0-9 and marking which one was done
				if (y[j] == 1) {
					y_val = j;
					results[1][j]++; //increasing the results second row at the column that corresponds with the y_val. If the correct number is 7, column 7 is incremented.
				}
			}
			// if the guess is correct, the corresponding column in the first row is incremented
			if (a_val == y_val) { results[0][a_val]++; }
		}
		// calculating the total number of inputs (total), the total guessed correctly (total_right), and the percentage correct (percentage).
		int total = (results[1][0] + results[1][1] + results[1][2] + results[1][3] + results[1][4] + results[1][5] + results[1][6] + results[1][7] + results[1][8] + results[1][9]);
		int total_right = (results[0][0] + results[0][1] + results[0][2] + results[0][3] + results[0][4] + results[0][5] + results[0][6] + results[0][7] + results[0][8] + results[0][9]);
		float percentage = ((float) total_right / total) * 100;
		System.out.println("0 = " + results[0][0] + "/" + results[1][0] 
		+ "\t1 = " + results[0][1] + "/" + results[1][1]  
		+ "\t2 = " + results[0][2] + "/" + results[1][2]  
		+ "\t3 = " + results[0][3] + "/" + results[1][3]  
		+ "\t4 = " + results[0][4] + "/" + results[1][4]  
		+ "\n5 = " + results[0][5] + "/" + results[1][5]  
		+ "\t6 = " + results[0][6] + "/" + results[1][6]  
		+ "\t7 = " + results[0][7] + "/" + results[1][7]  
		+ "\t8 = " + results[0][8] + "/" + results[1][8]  
		+ "\t9 = " + results[0][9] + "/" + results[1][9] 
		+ "\nAccuracy = " + total_right + "/" +  total + " = " + percentage + "%");
		
	}
	
	// Doing the stochastic gradient descent
	public void stochastic_gradient_descent (String data_location) {
		// Set up for SGD. Gets the data and does an initial test
		Pair[] training_data = getTrainingData(data_location, 60000);
		System.out.println("Initial run through data with unchanged weights and biases...");
		feedforward(training_data);
		
		// Begin actual sgd
		int length = training_data.length;
		// iterate through training data based on epochs
		Random r = new Random();
		for(int i = 0; i < epochs; i++) {
			// shuffle training data
			for(int j = 0; j < length - 1; j++) {
				int k = ThreadLocalRandom.current().nextInt(j, training_data.length);
				Pair a = training_data[k];
				training_data[k] = training_data[j];
				training_data[j] = a;
			}
			// turn training data into # of mini batches declared
			Pair[][] mini_batches = new Pair[length/batch_size][batch_size];
			int data = 0;
			for(int j = 0; j < length/batch_size; j++) {
				for(int k = 0; k < batch_size; k++) {
					mini_batches[j][k] = training_data[data];
					data++;
				}
			}
			// for each mini batch, update the weights and biases
			for(int j = 0; j < length/batch_size; j++) {
				Pair[] mini_batch = new Pair[10];
				mini_batch = mini_batches[j];
				update_batches(mini_batch);	
				System.out.println("mini batch complete");
				
			}
			
			System.out.println("\n\nfinished epoch " + (i+1));
			
			// Runs data through updated weights and biases
			feedforward(training_data);
		}
	}
	
	// Updates the mini batches passed in
	private void update_batches (Pair[] mini_batch) {
		float[][] weight_grad1 = new float[30][784];
		float[][] weight_grad2 = new float[10][30];
		float[] bias_grad1 = new float[30];
		float[] bias_grad2 = new float[10]; 
		// for each pair in the array
		for (int i = 0; i < 10; i++) {
			// Gets changes in weight and bias gradients with backpropagation!!!!
			Pair[] deltas = backpropagation(mini_batch[i]);
			// The first pair are the deltas for weight and bias gradients 1 and the second pair are the deltas for weight and bias gradients 2.
			Pair delta1 = deltas[0];
			Pair delta2 = deltas[1];
			// Now update the weights and biases for this batch.
			weight_grad1 = matrix_add(weight_grad1, delta1.getX());
			weight_grad2 = matrix_add(weight_grad2, delta2.getX());
			bias_grad1 = vector_add(bias_grad1, delta1.getY());
			bias_grad2 = vector_add(bias_grad2, delta2.getY());
		}
		// updates layers with the changed weight and bias gradients
		update(weight_grad1, bias_grad1, 1);
		update(weight_grad2, bias_grad2, 2);
	}
	
	private Pair[] backpropagation (Pair input) {
		
		float[][] delta_wg1 = new float[30][784];
		float[][] delta_wg2 = new float[10][30];
		float[] delta_bg1 = new float[30];
		float[] delta_bg2 = new float[10];
		
		//First is feedforward
		float[] a = input.getZ();
		float[] y = input.getY();
		float[][] activations = new float[3][]; 
		float[][] z_values = new float[2][];
		activations[0] = a;
		
		float[] z = vector_add(vector_mult(weight1, a, 0f), bias1);
		z_values[0] = z;
		
		a = sigmoid(z);
		activations[1] = a;
		// vector
		z = vector_add(vector_mult(weight2, a, 0f), bias2);
		z_values[1] = z;
		
		a = sigmoid(z);
		activations[2] = a;
		//System.out.println("Activations: " + Arrays.deepToString(activations) + " \nZ_values: " + Arrays.deepToString(z_values));
		
		//Now its the backward pass!!!!!!!!
		float[] delta = new float[10];
		float[] sp = sigmoid_prime(z_values[1]);
		for (int i = 0; i < 10; i++) { delta[i] = (activations[2][i] - y[i]) * (sp[i]); }
		delta_bg2 = delta;
		delta_wg2 = matrix_mult(null, delta, activations[1], 0f);
		//System.out.println("after first layer of back prop!!!!!\ndelta = " + Arrays.toString(delta) + "\nbiasGradient delta = " + Arrays.toString(delta_bg2) + "\nweightGradient delta = " + Arrays.deepToString(delta_wg2) + "\n");
		
		sp = sigmoid_prime(z_values[0]);
		delta = vector_mult(weight2, delta, 0f);
		for (int i = 0; i < 30; i++) { delta[i] = delta[i] * sp[i]; }
		delta_bg1 = delta;
		delta_wg1 = matrix_mult(null, delta, activations[0], 0f);		
		//System.out.println("after second layer of back prop!!!!!\ndelta = " + Arrays.toString(delta) + "\nbiasGradient delta = " + Arrays.toString(delta_bg1) + "\nweightGradient delta = " + Arrays.deepToString(delta_wg1) + "\n\n");
		
		Pair[] deltas = new Pair[2];
		Pair delta_1 = new Pair(delta_wg1, delta_bg1);
		Pair delta_2 = new Pair(delta_wg2, delta_bg2);
		deltas[0] = delta_1;
		deltas[1] = delta_2;
		
		return deltas;
		
	}
	
	/* VECTOR AND MATRIX FUNCTIONS */
	// returns a matrix
	private float[][] matrix_mult(float[][] w, float[] x, float[] y, float z) {
		// i don't have any cases besides two vectors or a matrix and a scalar so check which case it is and then keep on trucking
		boolean twoVectors = (x == null) ? false : true;
		if (twoVectors) {
			int lenX = x.length; //ex: 10 meaning a 10x1 array
			int lenY = y.length; //ex: 30 meaning a 30x1 array
			float [][] result = new float[lenX][lenY]; // y will be treated as though it is transposed creating a 10x30 array here :)
			// go through the two vectors and multiply them together
			for (int j = 0; j < lenX; j++) {
				for (int k = 0; k < lenY; k++) {
					result[j][k] = x[j] * y[k];
				}
			}
			return result;
			
		} else {
			// get the SIZE of w
			int lenW = w.length;
			int widthW = w[0].length;
			// not going to use a result vector becuase I'm just going to edit w directly
			// Go through w and multiply each index by the scalar
			for (int j = 0; j < lenW; j++) {
				for (int k = 0; k < widthW; k++) {
					w[j][k] = w[j][k] * z;
				}
			}
			return w;
		}
	}
	
	// will return a vector
	private float[] vector_mult(float[][] x, float[] y, float z) {
		// If z is 0, that means its a matrix * a vector
		if (z == 0f) {
			boolean transpose = false;
			// first double check that the second [] matches the y length
			if (x[0].length != y.length) {
				// if they don't match check if the other one does (so you can transpose it)
				if (x.length == y.length) {
					transpose = true;
				}
			}
			// now do the MATH
			// sets up how the array is handled. if its being transposed, it should iterate through a different way
			int lenX = x.length ; 
			int widthX = x[0].length ;
			// the size is different depending on if the array is transposed
			float[] result = transpose ? new float[widthX] : new float[lenX];
			if (!transpose) {
				for (int j = 0; j < lenX; j++) {
					float sum = 0;
					for (int k = 0; k < widthX; k++) {
						sum = sum + (x[j][k] * y[k]);
					}
					result[j] = sum;
				}
			} else { 
				for (int j = 0; j < widthX; j++) {
					float sum = 0;
					for (int k = 0; k < lenX; k++) {
						sum = sum + (x[k][j] * y[k]);
					}
					result[j] = sum;
				}
			}
			return result;
			
		} else {// If z isn't 0, that means its a vector * a scalar
			// go through the vector and multiply each index by a scalar
			int lenY = y.length;
			for (int j = 0; j < lenY; j++) {
				y[j] = y[j] * z;
			}
			return y;
		}
	}
	
	// Returns a matrix
	private float[][] matrix_add(float[][] x, float[][] y) {
	// this is assuming that the matrices are the same size. if they aren't i have way bigger problems :-)
		int len = x.length;
		int width = x[0].length;
		// no result vector because I'll just modify x
		// Goes through and just... adds those bad boys together
		for (int j = 0; j < len; j++) {
			for (int k = 0; k < width; k++) {
				x[j][k] = x[j][k] + y[j][k];
			}
		}
		
		return x;
	}
	
	// Returns a vector
	private float[] vector_add(float[] x, float[] y) {
		int len = x.length;
		// Once again just goes right on through and adds those suckers together
		for (int j = 0; j < len; j++) {
			x[j] = x[j] + y[j];
		}
		return x;
	}
	
	// Returns a matrix
	private float[][] matrix_sub(float[][] x, float[][] y) {
		int len = x.length;
		int width = x[0].length;
		// no result vector because I'll just modify x
		// Same as adding but subtracting
		for (int j = 0; j < len; j++) {
			for (int k = 0; k < width; k++) {
				x[j][k] = x[j][k] - y[j][k];
			}
		}
		
		return x;
	}
	
	// Returns a vector
	private float[] vector_sub(float[] x, float[] y) {
		int len = x.length;
		// Same as adding but subracting
		for (int j = 0; j < len; j++) {
			x[j] = x[j] - y[j];
		}
		return x;
	}
	
	/* S I G M O I D   F U N C T I O N S */
	// Implements sigmoid function: (1/1+e^-z)
	private float[] sigmoid(float[] z) {
		int len = z.length;
		// Math.exp() does e^whatever
		// So i go through here and for every item in z, i sigmoid it and then return the results
		float[] result = new float[len];
		for (int j = 0; j < len; j++) {
			double k = (double) -z[j];
			k = Math.exp(k);
			k =  1/(1+k);
			result[j] = (float) k;
		}
		return result;
	}
	
	// Implements sigmoid prime function: sig(z) * (1-sig(z))
	private float[] sigmoid_prime(float[] z) {
		// I go through here and for every item in z, i sigmoid PRIME! it and then return the results
		int len = z.length;
		float[] sig = sigmoid(z);
		for (int j = 0; j < len; j++) {
			z[j] = sig[j] * (1- sig[j]);
		}
		
		return z;
	}
	
	/* UPDATES THE WEIGHT AND BIAS VALUES */
	private void update(float[][] wg, float[] bg, int layer) {
		float div = learning_rate / batch_size;
		// different layers means different vectors and matrices
		// goes through weights and biases and applies the update math to each item
		// new = old - (LR/BS) * (sum of gradients)
		switch (layer) {
			case 1: // weight and bias 1
				for (int j = 0; j < 30; j++) {
					for (int k = 0; k < 784; k++){
						weight1[j][k] = weight1[j][k] - (wg[j][k] * div);
					}
					bias1[j] = bias1[j] - (bg[j] * div);
				}
				break;
			case 2: // weight and bias 2
				for (int j = 0; j < 10; j++) {
					for (int k = 0; k < 30; k++){
						weight2[j][k] = weight2[j][k] - (wg[j][k] * div);
					}
					bias2[j] = bias2[j] - (bg[j] * div);
				}
				break;
		}
	}
}
 
// The basis of this class is from a stackOverflow question. I changed it to suit this project but I did want to be transparent
// I'm using it to hold tuples. I don't know why I did it this way? I was very tired when I did this specific part and then it was too big of a hassle to reformat
class Pair {
	private float[][] x;
	private float[] y;
	private float [] z;
	
	public Pair(float[][] x, float[] y) { // used to pair up weights and biases
		this.x = x;
		this.y = y;
		z = null;
	}	
	
	public Pair(float[] z, float[] y) { // used to pair up inputs and outputs
		this.z = z;
		this.y = y;
		x = null;
	}

	public Pair()
	{

	}

	public float[][] getX() {
		return x;
	}

	public void setX(float[][] x) {
		this.x = x;
	}

	public float[] getY() {
		return y;
	}

	public void setY(float[] y) {
		this.y = y;
	}	
	
	public float[] getZ() {
		return z;
	}

	public void setZ(float[] z) {
		this.z = z;
	}
 }