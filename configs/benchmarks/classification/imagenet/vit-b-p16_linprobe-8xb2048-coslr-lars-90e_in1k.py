_base_ = 'vit-b-p16_linprobe-8xb512-coslr-sgd-90e_in1k.py'

# dataset
data = dict(imgs_per_gpu=512, workers_per_gpu=8)

# optimizer
optimizer = dict(
    type='LARS', lr=0.1 * 16384 / 256, weight_decay=0.0, momentum=0.9)

# learning policy
lr_config = dict(min_lr=0.0)

# runtime
log_config = dict(
    interval=25, hooks=[
        dict(type='TextLoggerHook'),
    ])
runner = dict(type='EpochBasedRunner', max_epochs=90)
