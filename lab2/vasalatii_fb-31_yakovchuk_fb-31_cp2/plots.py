import seaborn as sns
import matplotlib.pyplot as plt

def barplot(x, y, title:str, x_label:str, y_label:str, should_show_values:bool, values_rot: int = 0, save_path:str= None):
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="whitegrid")

    ax = sns.barplot(x=x, y=y, palette="viridis", hue=x, legend=False)
    if should_show_values: 
        for container in ax.containers:
            ax.bar_label(
                container, 
                labels = [str(int(v)) if isinstance(v, float) and v.is_integer() else f"{v:.4f}" if isinstance(v, float) else str(v) for v in container.datavalues],
                padding=2, fontsize=10, rotation=values_rot
            )

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xticks(range(len(x)), labels=x, rotation=45)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)

    if save_path:
        plt.savefig(save_path)

    plt.show()
