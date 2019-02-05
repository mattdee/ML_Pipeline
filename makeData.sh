# Make random efile data
unset RUNTIME
export RUNTIME=$(date +%m%d%y%H%M%s%N)

export GROSS_INCOME=$((0000 + RANDOM % 500000))
export DEDUCTIONS=$((100 + RANDOM % 100000))
export TAXES_PAID=$((100 + RANDOM % 999999))
export REFUND_AMT=$((100 + RANDOM % 999999))
export TAXES_OWED=$((100 + RANDOM % 999999))


echo $GROSS_INCOME,$DEDUCTIONS,$TAXES_PAID,$REFUND_AMT,$TAXES_OWED >/tmp/ml_pipe/$RUNTIME.csv