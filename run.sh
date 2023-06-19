MODEL_PATH=/bigone/gpt_neox

python train.py \
    --dataset_name wikitext \
    --dataset_config_name wikitext-2-raw-v1 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --output_dir $MODEL_PATH \
    --overwrite_output_dir \
    --num_train_epochs 2 \
    --logging_steps 10 \
    --block_size 512 \

