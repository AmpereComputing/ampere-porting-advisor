#!/bin/bash


function check_integrity() {
    _prog_lang=$1
    _baseline_json=$2
    _app_html=$3
    _v_a=(`jq ".$1.integrity[]" $2`)
    for ((_idx=0;_idx<`jq ".$1.integrity | length" $2`;_idx++));
    do
        _k=`jq -r ".$1.integrity | keys_unsorted" $2 | jq -r ".[$_idx]"`
	_res=`grep "$_k" "$_app_html" | wc -l`
	echo -e "-- [$_k] target: ${_v_a[_idx]}, found: $_res"
        if [ $_res -lt ${_v_a[_idx]} ]; then
            echo "**FAILED**: integrity check test" && exit 1
        fi
    done
    echo "**PASSED**: integrity check test"
}

function check_prompts() {
    _prog_lang=$1
    _baseline_json=$2
    _app_html=$3
    _v_a=(`jq -c ".$1.prompts[]" $2`)
    for ((_idx=0;_idx<`jq ".$1.prompts | length" $2`;_idx++));
    do
        _prompt=`jq -r ".$1.prompts" $2 | jq -r ".[$_idx]"`
        if grep --quiet "$_prompt" "$_app_html"
        then
            echo -e "-- ["$_prompt"] found"
        else
            echo -e "-- ["$_prompt"] NOT found"
	    echo "**FAILED**: prompts check test" && exit 1
        fi
    done
    echo "**PASSED**: prompts check test"
}

FILE_NAME=`./getBinaryName.sh`
chmod +x ./dist/$FILE_NAME

APP_DIR='sample-applications'
BASELINE_JSON='tests-baseline/sample_applications_test.json'


#for prog_langs in BASELINE_JSON, E.g. python go c_cpp java
for ((idx=0;idx<`jq ". | length" $BASELINE_JSON`;idx++));
do
    prog_lang=`jq -r ". | keys" $BASELINE_JSON | jq -r ".[$idx]"`
    dl_type=`jq -r ".$prog_lang.type" $BASELINE_JSON`
    dl_url=`jq -r ".$prog_lang.url" $BASELINE_JSON`
    dl_app=`jq -r ".$prog_lang.app" $BASELINE_JSON`

    [ ! -d "$APP_DIR/$prog_lang" ] && mkdir -p $APP_DIR/$prog_lang
	
    if [ 'git' == $dl_type ]; then
        DL_BRANCH=`jq -r ".$prog_lang.branch" $BASELINE_JSON`
        [ ! -d "$APP_DIR/$prog_lang/$dl_app" ] && git -C $APP_DIR/$prog_lang clone --depth 1 --branch $DL_BRANCH $dl_url
    elif [ 'wget' == $dl_type ]; then
        dl_file=$(basename "$dl_url")
        [ ! -f "$APP_DIR/$prog_lang/$dl_file" ] && wget $dl_url -P $APP_DIR/$prog_lang/
        [ ! -d "$APP_DIR/$prog_lang/$dl_app" ] && tar zxf $APP_DIR/$prog_lang/$dl_file -C $APP_DIR/$prog_lang/
    else
        echo "wrong download type"
    fi

    echo "Running $prog_lang application to HTML report"
    ./dist/$FILE_NAME $APP_DIR/$prog_lang/$dl_app --output $dl_app.html

    echo "Running integrity check for $prog_lang application's HTML report"
    check_integrity $prog_lang $BASELINE_JSON "$dl_app.html"
    [ $? -ne 0 ] && exit 1
    
    echo "Running prompts check for $prog_lang application's HTML report"
    check_prompts $prog_lang $BASELINE_JSON "$dl_app.html"
    [ $? -ne 0 ] && exit 1
done
exit 0
