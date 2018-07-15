import pandas as pd
import altair as alt

COLOR1, COLOR2, COLOR3 = ['#ef8a62', '#67a9cf', "#f7f7f7"]


def get_epoch_max_val_acc(data):
    """Gets the epoch with the highest validation accuracy."""
    df_val = data[data['data'] == 'validation']
    return int(df_val[df_val['acc'] == df_val['acc'].max()]['epoch'])


def plot_accuracy(data, output_path='accuracy.png', truncate_y=True, title='', width=500, height=300, output_scale_factor=2):
    max_val_epoch = get_epoch_max_val_acc(data)

    base = alt.Chart(data).mark_line().encode(
        alt.X('epoch', type='ordinal', axis=alt.Axis(title='Epochs')),
        alt.Y('acc', type='quantitative',
              scale=alt.Scale(zero=not truncate_y), axis=alt.Axis(title='Accuracy')),
        alt.Color('data', type='nominal', legend=alt.Legend(
            title=None, orient="bottom-right"), scale=alt.Scale(
            domain=['training', 'validation'],
            range=[COLOR1, COLOR2]))
    )

    highlight = alt.Chart(data).mark_rule(color=COLOR2).encode(
        x='epoch:O',
        opacity=alt.value(0.4)
    ).transform_filter(
        alt.FieldEqualPredicate(field='data', equal='validation')).transform_filter(
        alt.FieldEqualPredicate(field='epoch', equal=max_val_epoch)
    )

    highlight2 = alt.Chart(data).mark_circle(color=COLOR2).encode(
        x='epoch:O',
        y='acc',
        size=alt.value(25)
    ).transform_filter(
        alt.FieldEqualPredicate(field='data', equal='validation')).transform_filter(
        alt.FieldEqualPredicate(field='epoch', equal=max_val_epoch)
    )

    annotation = alt.Chart(data).mark_text(
        align='center',
        baseline='top',
        fontSize=12,
        dy=10,
        color=COLOR2
    ).encode(
        x='epoch:O',
        y='acc',
        text=alt.Text('acc', format=".4f")
    ).transform_filter(
        alt.FieldEqualPredicate(field='data', equal='validation')
    ).transform_filter(
        alt.FieldEqualPredicate(field='epoch', equal=max_val_epoch)
    )

    # combine parts and configure / style
    chart = alt.layer(
        base,
        annotation,
        highlight,
        highlight2
    ).properties(
        width=width,
        height=height,
        title=title,
        background='white'
    ).configure_legend(fillColor='white', strokeColor='white', padding=5
                       ).configure_axis(gridColor=COLOR3)

    chart.save(output_path, scale_factor=output_scale_factor)


def plot_loss(data, output_path='loss.png'):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    chart = alt.Chart(data)
    chart.save(output_path)
