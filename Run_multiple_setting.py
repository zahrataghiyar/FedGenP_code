import subprocess

# List of different settings you want to use
settings_list = [
'--dataset Mnist-alpha1-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset Mnist-alpha0.1-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset Mnist-alpha0.01-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset Mnist-alpha1-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset Mnist-alpha0.1-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset Mnist-alpha0.01-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset Mnist-alpha1-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset Mnist-alpha0.1-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset Mnist-alpha0.01-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset Mnist-alpha1-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset Mnist-alpha0.1-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset Mnist-alpha0.01-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset EMnist-alpha1-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset EMnist-alpha0.1-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset EMnist-alpha0.01-ratio1 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset EMnist-alpha1-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset EMnist-alpha0.1-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset EMnist-alpha0.01-ratio1 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset EMnist-alpha1-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset EMnist-alpha0.1-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset EMnist-alpha0.01-ratio1 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset EMnist-alpha1-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset EMnist-alpha0.1-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3', 
'--dataset EMnist-alpha0.01-ratio1 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 ',

'--dataset CelebA-user25-agg10 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 25 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 15 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 10 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedAvg --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 5 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',


'--dataset CelebA-user25-agg10 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 25 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 15 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 10 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGen --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 5 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',


'--dataset CelebA-user25-agg10 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 25 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 15 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 10 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedGenP --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 5 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',


'--dataset CelebA-user25-agg10 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 25 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 20 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 15 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 10 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
'--dataset CelebA-user25-agg10 --algorithm FedEnsemble --batch_size 32 --num_glob_iters 300 --local_epochs 20 --num_users 5 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3',
]

# Loop through the settings and run main.py for each setting
for i, settings in enumerate(settings_list):
    print('running this setting: ', settings)
    with open('DoneSettings.txt', 'a') as file:
        # Write the string to the file
        txt = str(i) + '. ' + settings
        file.write(txt+ "\n")
    command = f"python main.py {settings}"
    subprocess.run(command, shell=True)